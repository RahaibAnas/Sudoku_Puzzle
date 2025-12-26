# 🧩 Sudoku Validator

A lightweight Python utility powered by **NumPy** to verify if a $9 \times 9$ grid satisfies the fundamental rules of Sudoku.

---

## 🧐 Features
* **Row & Column Integrity**: Ensures every row and column contains digits 1-9 without duplicates using `np.unique`.
* **Subgrid Validation**: Specifically checks each $3 \times 3$ block to ensure the sum equals 45.
* **Efficient Logic**: Uses NumPy slicing for high-performance array traversal.

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/your-username/sudoku-validator.git](https://github.com/your-username/sudoku-validator.git)
   cd sudoku-validator
   
