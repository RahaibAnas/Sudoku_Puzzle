<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sudoku Validator README</title>
</head>
<body>

    <h1>Sudoku Validator</h1>
    <p>
        A Python-based utility that uses the <strong>NumPy</strong> library to validate whether a 9x9 grid follows the standard rules of a Sudoku puzzle. 
        It checks rows, columns, and 3x3 subgrids for mathematical correctness.
    </p>

    <hr>

    <h2>🧐 Features</h2>
    <ul>
        <li><strong>Row &amp; Column Validation:</strong> Uses <code>np.unique</code> to ensure every row and column contains exactly 9 unique digits.</li>
        <li><strong>3x3 Subgrid Validation:</strong> Uses array slicing to verify that each of the nine 3x3 subgrids sums to exactly 45.</li>
        <li><strong>NumPy Power:</strong> Leverages efficient array manipulations for high-speed verification.</li>
    </ul>

    

    <h2>🛠️ Installation</h2>
    <p>1. <strong>Clone the repository:</strong></p>
    <pre><code>git clone https://github.com/your-username/sudoku-validator.git
cd sudoku-validator</code></pre>

    <p>2. <strong>Install dependencies:</strong></p>
    <p>This project requires the NumPy library installed in your Python environment.</p>
    <pre><code>pip install numpy</code></pre>

    <h2>🚀 Usage</h2>
    <p>
        The script contains a predefined NumPy array. You can toggle between a "correct" and "incorrect" Sudoku grid by commenting or uncommenting the array definitions inside <code>sudoku_puzzle.py</code>.
    </p>
    <p>To run the validator, execute the following command in your terminal:</p>
    <pre><code>python sudoku_puzzle.py</code></pre>

    <h3>Internal Logic Summary:</h3>
    <ul>
        <li><code>arr_uni(arr)</code>: Confirms that all 9 rows and 9 columns contain unique elements.</li>
        <li><code>arr_sum(arr)</code>: Slices the grid into 3x3 blocks and verifies their mathematical sum.</li>
        <li><code>arr_sud()</code>: The main function that prints the final "Sudoku" or "Not Sudoku" status based on the checks.</li>
    </ul>

    <hr>

    <h2>📜 License</h2>
    <p>
        This project is open-source and available under the <strong>MIT License</strong>.
    </p>

</body>
</html>
