# Outlive Weather Master

## What is Outlive Weather Master?

Outlive Weather Master is a simple and easy to use API that allows you to see the weather of any city you want. You can use it to make a simple weather app or even a weather widget.

Live API is up at [wkuzx9.deta.dev](https://wkuzx9.deta.dev/weatherapi)

## API Documentation

This section defines the expected Input and the Output formats for the Outlive Weather service.

| API URL | Parameters | Return Type |
|---------|------------|--------------|
`http://localhost:8000/weather` | `city` | `JSON`|

## Installation

- Step 1: Enable a virtual environment

    ```bash
    python3 -m virtualenv venv
    ```

- Step 2: Install the dependencies

    ```bash
    pip install -r requirements.txt
    ```

- Step 3: Run the application

    ```bash
    uvicorn main:app --reload
    ```

- Step 4: Checkout Swagger UI

    Open the browser and navigate to `http://127.0.0.1:8000/weatherapi`

## Useful for Developers

- Get the live weather of a city using the API
- Create a weather widget using the API
- Useful for implementation inside a website

## Feedback

If you have any feedback, please reach out to us at sagnikdas2305@gmail.com

## Contributing

Contributions are welcome! Please open an issue or pull request on GitHub.
