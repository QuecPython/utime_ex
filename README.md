# QuecPython Enhanced Time & TimeZone

[中文](README_ZH.md) | English

## Overview

QuecPython utime method can only support the east and west 12 time zone, but in practice, some countries with borders across the international date line in order to maintain national date unity, the original territorial date of UTC-11 is pushed forward by one day, that is, from UTC-11 plus 24H, is UTC+13. This method can extend the time zone to UTC-12 to UTC+14.

At the same time, the utime method does not have a convenient way to set the time, so it needs to call the API of setting the time in RTC separately, and it needs to convert the date format. This method provides a method of obtaining/setting the local time in a consistent format.

Finally, this method provides a more flexible mktime method, which can add the time zone parameter and directly obtain the time stamp of the specified time zone.

## Usage

- [API Reference Manual](./docs/en/API_Reference.md)

## Contribution

We welcome contributions to improve this project! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License

This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for details.

## Support

If you have any questions or need support, please refer to the [QuecPython documentation](https://python.quectel.com/doc/en) or open an issue in this repository.
