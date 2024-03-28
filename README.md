# FastAPI TODO API

This repository contains a simple TODO API built with FastAPI in Python.

## Getting Started

Follow these steps to set up and run the TODO API on your local machine.

### Prerequisites

- Python 3.x installed on your system

### Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2. Create a virtual environment:

    ```bash
    python -m venv env
    ```

3. Activate the virtual environment:

    ```bash
    # For Unix/Linux
    source env/bin/activate

    # For Windows
    env\Scripts\activate
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the FastAPI TODO API:

    ```bash
    uvicorn app:app --host 127.0.0.1 --port 8000 --reload
    ```

    The API will start running locally at http://127.0.0.1:8000/.

2. Accessing the API:

    You can access the API using tools like curl, Postman, or your web browser. The API documentation (Swagger UI) is available at http://127.0.0.1:8000/docs.

### Deactivation (Optional)

If you want to deactivate the virtual environment, run:

```bash
deactivate
