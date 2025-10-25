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
        Joint joint1(*bus, device_address);
        std::cout << "Created joint with address 0x" << std::hex << (int)device_address << std::dec << std::endl;

        // // Call get_angle_radians without passing bus
        // double angle = joint1.get_angle_radians();
        // std::cout << "Angle: " << angle << " radians" << std::endl;

        // Write motor direction
        joint1.write_motor_direction(0x01);
        
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}