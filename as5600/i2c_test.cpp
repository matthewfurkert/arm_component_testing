#include "i2c_comms.hpp"
#include <iostream>
#include <memory>

int main() {
    try {
        // Set SMBus number
        int bus_number = 4;
        std::shared_ptr<SMBus> bus = open_bus(bus_number);
        std::cout << "Opened SMBus " << bus_number << std::endl;
        
        // Set address to 0x12
        uint8_t device_address = 0x12;
        Sensor sensor(device_address);
        std::cout << "Created sensor with address 0x" << std::hex << (int)device_address << std::dec << std::endl;
        
        // Call get_angle_radians
        double angle = sensor.get_angle_radians(*bus);
        std::cout << "Angle: " << angle << " radians" << std::endl;
        
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}