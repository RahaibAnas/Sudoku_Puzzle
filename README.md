<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sudoku Validator Documentation</title>
    <style>
        /* Professional Styling */
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #c9d1d9;
            background-color: #0d1117; /* GitHub Dark Mode Background */
            max-width: 800px;
            margin: 40px auto;
            padding: 0 20px;
        }

        h1, h2, h3 {
            color: #58a6ff;
            border-bottom: 1px solid #30363d;
            padding-bottom: 10px;
        }

        code {
            background-color: #161b22;
            padding: 0.2rem 0.4rem;
            border-radius: 6px;
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
            font-size: 85%;
        }

        pre {
            background-color: #161b22;
            padding: 16px;
            border-radius: 8px;
            overflow: auto;
            border: 1px solid #30363d;
        }

        pre code {
            background-color: transparent;
            padding: 0;
            color: #e6edf3;
        }

        ul {
            padding-left: 20px;
        }

        li {
            margin-bottom: 10px;
        }

        hr {
            height: 0.25em;
            background-color: #30363d;
            border: 0;
            margin: 24px 0;
        }

        strong {
            color: #f0f6fc;
        }
    </style>
</head>
<body>

    <h1>Sudoku Validator</h1>
    <p>
        A Python-based utility that uses the <strong>NumPy</strong> library to validate whether a 9x9 grid follows the standard rules of a Sudoku puzzle.
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
    <pre><code>pip install numpy</code></pre>

    <h2>🚀 Usage</h2>
    <p>Execute the script to check the hardcoded Sudoku array:</p>
    <pre><code>python sudoku_puzzle.py</code></pre>

    <hr>

    <h2>📜 License</h2>
    <p>Distributed under the <strong>MIT License</strong>.</p>

</body>
</html>
