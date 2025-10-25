#ifndef I2C_COMMS_HPP
#define I2C_COMMS_HPP

#include "smbus.hpp"
#include <cstdint>
#include <vector>
#include <stdexcept>
#include <memory>
#include <cmath>

#define SENSOR_STATUS		1
#define SENSOR_RAW_ANGLE	3
#define MOTOR_DIRECTION		5
#define MOTOR_SPEED			6

#define DATA_WRITE          1
#define DATA_READ           2

inline std::shared_ptr<SMBus> open_bus(int bus_number) {
    return std::make_shared<SMBus>(bus_number);
}

class Joint {
    SMBus& bus_;
    uint8_t slave_address_;

    std::vector<uint8_t> i2c_read(uint8_t data_size, uint8_t data_direction, uint8_t data_address) const {
        try {
            // Combine write and read into a single transaction to avoid repeated START conditions
            I2cMsg write_msg = I2cMsg::write(slave_address_, {data_size, data_direction, data_address});
            I2cMsg read_msg = I2cMsg::read(slave_address_, data_size);
            
            // Single i2cRdwr call with both write and read messages
            bus_.i2cRdwr({write_msg, read_msg});

            auto data = read_msg.getData();
            if (data.size() != data_size) {
                throw std::runtime_error("Read size mismatch");
            }
            return data;
        } catch (const std::exception& e) {
            throw std::runtime_error("I2C read failed: " + std::string(e.what()));
        }
    }
    void i2c_write(uint8_t data_size, uint8_t data_direction, uint8_t data_address, const std::vector<uint8_t>& data) const {
        try {
            // Prepare the data buffer
            std::vector<uint8_t> buffer = {data_size, data_direction, data_address};
            buffer.insert(buffer.end(), data.begin(), data.end());

            // Create write message
            I2cMsg write_msg = I2cMsg::write(slave_address_, buffer);
        
            // Execute the I2C transaction
            bus_.i2cRdwr({write_msg});

        } catch (const std::exception& e) {
            throw std::runtime_error("I2C read failed: " + std::string(e.what()));
        }
    }

    uint16_t read_raw_angle() const {
        auto data = i2c_read(2, DATA_READ, SENSOR_RAW_ANGLE);
        return (static_cast<uint16_t>(data[0]) << 8) | data[1];
    }
    
public:
    explicit Joint(SMBus& bus, uint8_t address) : bus_(bus), slave_address_(address) {}
    
    uint16_t read_angle_sensor_status() const {
        auto data = i2c_read(2, DATA_READ, SENSOR_STATUS);
        return (static_cast<uint16_t>(data[0]) << 8) | data[1];
    }

    void write_motor_direction(uint16_t direction) const {
        std::vector<uint8_t> data = {static_cast<uint8_t>(direction & 0x0F)};
        i2c_write(1, DATA_WRITE, MOTOR_DIRECTION, data);
    }
    
    double get_angle_radians() const {
        return static_cast<double>(read_raw_angle()) * 2.0 * M_PI / 4096.0;
    }
};

#endif // I2C_COMMS_HPP