#include "pwm.hpp"
#include <iostream>
#include <chrono>
#include <thread>

int main() {
    try {
        PWM pwm(1, 0);                 // Initialize PWM object for chip 0, channel 0
        pwm.set_frequency(50);         // Set PWM frequency to 50 Hz
        pwm.set_duty_cycle(0.0);       // Set initial duty cycle to 0.0 (0%)
        pwm.set_polarity("normal");    // Set polarity to normal
        pwm.enable();                  // Enable the PWM signal

        for (int i = 0; i <= 10; i++) {
            double duty = i / 10.0;    // Calculate duty cycle: 0.0, 0.1, ..., 1.0
            pwm.set_duty_cycle(duty);  // Set the duty cycle
            printf("Current duty cycle: %.0f%%\n", duty * 100); // Print as percentage
            std::this_thread::sleep_for(std::chrono::seconds(1)); // Wait 1 second
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