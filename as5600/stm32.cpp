#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
#include <thread>
#include <chrono>
#include <cstdint>
#include "smbus.hpp"

std::vector<uint8_t> parseData(int argc, char* argv[], int start) {
    std::vector<uint8_t> data;
    for (int i = start; i < argc; i++) {
        int val = std::stoi(argv[i]);
        if (val < 0 || val > 255) throw std::out_of_range("Value out of range");
        data.push_back(val);
    }
    return data;
}

void printData(const std::string& prefix, uint8_t reg, const std::vector<uint8_t>& data) {
    std::cout << prefix << reg << ": ";
    for (size_t i = 0; i < data.size(); i++) {
        std::cout << "0x" << std::hex << std::uppercase << std::setfill('0') 
                  << std::setw(2) << (int)data[i] << std::dec;
        if (i < data.size() - 1) std::cout << " ";
    }
    std::cout << " (" << (int)data[0];
    for (size_t i = 1; i < data.size(); i++) std::cout << " " << (int)data[i];
    std::cout << ")" << std::endl;
}

bool i2cWrite(SMBus& bus, uint16_t addr, uint8_t reg, const std::vector<uint8_t>& data) {
    try {
        std::vector<uint8_t> tx = {reg};
        tx.insert(tx.end(), data.begin(), data.end());
        printData("Write to reg ", reg, data);
        bus.i2cRdwr({I2cMsg::write(addr >> 1, tx)});
        return true;
    } catch (const std::exception& e) {
        std::cerr << "Write failed: " << e.what() << std::endl;
        return false;
    }
}

bool i2cRead(SMBus& bus, uint16_t addr, uint8_t reg, uint8_t count, std::vector<uint8_t>& data) {
    try {
        bus.i2cRdwr({I2cMsg::write(addr >> 1, {reg})});
        std::this_thread::sleep_for(std::chrono::microseconds(100));
        I2cMsg readMsg = I2cMsg::read(addr >> 1, count);
        bus.i2cRdwr({readMsg});
        data = readMsg.getData();
        printData("Read from reg ", reg, data);
        return true;
    } catch (const std::exception& e) {
        std::cerr << "Read failed: " << e.what() << std::endl;
        return false;
    }
}

int main(int argc, char* argv[]) {
    if (argc < 4) {
        std::cout << "Usage:\n"
                  << "  " << argv[0] << " write <reg> <data...>  # Write data to register\n"
                  << "  " << argv[0] << " read <reg> <count>     # Read count bytes from register\n"
                  << "Registers: 0-9, Values: 0-255\n";
        return -1;
    }

    try {
        bool isWrite = (std::string(argv[1]) == "write");
        int reg = std::stoi(argv[2]);
        
        if (reg < 0 || reg > 9) {
            std::cerr << "Register must be 0-9\n";
            return -1;
        }

        SMBus bus(4);
        uint16_t addr = 0x12 << 1;
        
        std::cout << "I2C 0x" << std::hex << (addr >> 1) << std::dec 
                  << " every 1000ms (Ctrl+C to stop)\n";

        if (isWrite) {
            auto data = parseData(argc, argv, 3);
            if (reg + data.size() > 10) {
                std::cerr << "Data exceeds register bounds\n";
                return -1;
            }
            while (true) {
                i2cWrite(bus, addr, reg, data);
                std::this_thread::sleep_for(std::chrono::seconds(1));
            }
        } else {
            if (argc != 4) {
                std::cerr << "Read requires: read <reg> <count>\n";
                return -1;
            }
            int count = std::stoi(argv[3]);
            if (count < 1 || count > 10 || reg + count > 10) {
                std::cerr << "Invalid read count or exceeds bounds\n";
                return -1;
            }
            while (true) {
                std::vector<uint8_t> data;
                i2cRead(bus, addr, reg, count, data);
                std::this_thread::sleep_for(std::chrono::seconds(1));
            }
        }
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return -1;
    }
}