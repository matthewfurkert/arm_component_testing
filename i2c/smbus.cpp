#include "smbus.hpp"
#include <iostream>
#include <iomanip>
#include <vector>
#include <chrono>
#include <thread>
#include <cstdint>

const int DEVICE_AS5600 = 0x36;

uint16_t ReadRawAngle(SMBus& bus) {
    std::vector<uint8_t> data = bus.readI2cBlockData(DEVICE_AS5600, 0x0C, 2);
    if (data.size() != 2) {
        throw std::runtime_error("Failed to read 2 bytes for angle");
    }
    return (static_cast<uint16_t>(data[0]) << 8) | data[1];
}

uint16_t ReadMagnitude(SMBus& bus) {
    std::vector<uint8_t> data = bus.readI2cBlockData(DEVICE_AS5600, 0x1B, 2);
    if (data.size() != 2) {
        throw std::runtime_error("Failed to read 2 bytes for magnitude");
    }
    return (static_cast<uint16_t>(data[0]) << 8) | data[1];
}

int main() {
    try {
        SMBus bus(3);  // Open I2C bus 3
        while (true) {
            uint16_t raw_angle = ReadRawAngle(bus);
            uint16_t magnitude = ReadMagnitude(bus);
            double angle_deg = static_cast<double>(raw_angle) * 360.0 / 4096.0;
            std::cout << "Raw angle: " << std::setw(4) << raw_angle
                      << " m=" << std::setw(4) << magnitude
                      << " " << std::fixed << std::setprecision(2) << std::setw(6) << angle_deg << " deg  "
                      << std::endl;
            std::this_thread::sleep_for(std::chrono::seconds(1));
        }
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}