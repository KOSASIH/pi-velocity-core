import sys
import logging
import pi_velocity

def main():
    # Initialize the Pi-Velocity system
    pi_velocity.init()

    # Start the Pi-Velocity system
    pi_velocity.start()

if __name__ == '__main__':
    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

    try:
        main()
    except Exception as e:
        logging.error(f'Error in main: {e}')
        sys.exit(1)
