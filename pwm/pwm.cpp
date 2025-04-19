#include "pwm.hpp"
#include <iostream>
#include <chrono>
#include <thread>
#include <cmath>

int main() {
    try {
        PWM pwm(2, 0);                  // Initialize PWM object for chip 2, channel 0
        pwm.set_frequency(50);         // Set PWM frequency to 50 Hz
        pwm.set_duty_cycle(0.0);       // Set initial duty cycle to 0.0
        pwm.set_polarity("normal");    // Set polarity to normal
        pwm.enable();                  // Enable the PWM signal
        int direction = 1;             // Initial direction (1 for increasing, -1 for decreasing)
        double current_duty = 0.0;     // Current duty cycle value

        while (true) {
            current_duty += 0.01 * direction;                     // Adjust duty cycle
            current_duty = std::round(current_duty * 100.0) / 100.0; // Round to 2 decimal places
            pwm.set_duty_cycle(current_duty);                     // Update PWM duty cycle
            if (current_duty == 0.2) {                            // Check upper limit
                direction = -1;                                   // Reverse direction
            } else if (current_duty == 0.0) {                     // Check lower limit
                direction = 1;                                    // Reverse direction
            }
            std::this_thread::sleep_for(std::chrono::milliseconds(50)); // Delay 50 ms
        }
    } catch (const PWMError& e) {
        std::cerr << "PWMError: " << e.what() << std::endl;
        return 1;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}