# FastAPI - Patient Management System 

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)

A modern, scalable, and robust **Patient Management System API** built with **FastAPI** and **Pydantic** for managing patient records efficiently. This API allows you to create, read, update, delete, and sort patient data stored in a JSON file, with built-in validation and computed fields like BMI and health verdicts.

---

## ✨ Features

- **CRUD Operations**: Create, Read, Update, and Delete patient records.
- **Data Validation**: Uses **Pydantic** for strict type checking and validation of patient data.
- **Computed Fields**: Automatically calculates BMI and assigns a health verdict (Underweight, Normal, Obese).
- **Sorting**: Sort patient records by height, weight, or BMI in ascending or descending order.
- **Error Handling**: Comprehensive error responses for invalid inputs or missing records.
- **FastAPI Integration**: High-performance API with automatic OpenAPI documentation.
- **JSON Storage**: Persistent storage of patient data in a JSON file.

---

## 🛠️ Tech Stack

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.6+.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Python**: Core programming language for the application.
- **JSON**: Lightweight data storage for patient records.

---

## 📂 Project Structure

```bash
├── main.py          # Main API implementation with CRUD and sorting endpoints
├── main2.py         # Simplified API version with basic endpoints
├── paitent.json     # JSON file for storing patient data
├── README.md        # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/PrabhanshuKamal2121/patient-management-api.git
   cd patient-management-api
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi uvicorn pydantic
   ```

4. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API**:
   - Open your browser and navigate to `http://127.0.0.1:8000/docs` for the interactive Swagger UI.
   - Alternatively, use tools like **Postman** or **cURL** to interact with the API.

---

## 📖 API Endpoints

| Method | Endpoint                | Description                              | Example Query                  |
|--------|-------------------------|------------------------------------------|--------------------------------|
| GET    | `/`                     | Welcome message                          | `http://127.0.0.1:8000/`       |
| GET    | `/about`                | About the API                            | `http://127.0.0.1:8000/about`  |
| GET    | `/view`                 | View all patients                        | `http://127.0.0.1:8000/view`   |
| GET    | `/patient/{patient_id}` | View a specific patient by ID            | `http://127.0.0.1:8000/patient/P001` |
| GET    | `/sort`                 | Sort patients by height, weight, or BMI  | `http://127.0.0.1:8000/sort?sort_by=height&order=desc` |
| POST   | `/create`               | Create a new patient                     | Requires JSON payload          |
| PUT    | `/edit/{patient_id}`    | Update an existing patient               | Requires JSON payload          |
| DELETE | `/delete/{patient_id}`  | Delete a patient by ID                   | `http://127.0.0.1:8000/delete/P001` |

### Example POST Request (Create Patient)

```json
{
  "id": "P006",
  "name": "John Doe",
  "city": "Delhi",
  "age": 25,
  "gender": "male",
  "height": 1.75,
  "weight": 70.5
}
```

---

## 🧪 Testing the API

1. Use the **Swagger UI** at `http://127.0.0.1:8000/docs` to test endpoints interactively.
2. Use **Postman** or **cURL** for manual testing.
3. Example cURL command to create a patient:
   ```bash
   curl -X POST "http://127.0.0.1:8000/create" -H "Content-Type: application/json" -d '{"id":"P006","name":"John Doe","city":"Delhi","age":25,"gender":"male","height":1.75,"weight":70.5}'
   ```

---

## 📊 Sample Data

The `paitent.json` file contains sample patient records like:

```json
{
  "P001": {
    "name": "Ananya Verma",
    "city": "Guwahati",
    "age": 28,
    "gender": "female",
    "height": 1.65,
    "weight": 90.0,
    "bmi": 33.06,
    "verdict": "Obese"
  },
  ...
}
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

---

## 📝 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

Made by **Prabhanshu Kamal**  
For any questions or collaborations → [prabhanshukamal2121@gmail.com](mailto:prabhanshukamal2121@gmail.com)  
GitHub: [github.com/PrabhanshuKamal2121](https://github.com/PrabhanshuKamal2121)

---

## 🙌 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the amazing framework.
- [Pydantic](https://pydantic-docs.helpmanual.io/) for robust data validation.
- [Python](https://www.python.org/) for being the backbone of this project.
- [Shields.io](https://shields.io/) for beautiful badges.

---

**Built with ❤️ by Prabhanshu Kamal**
