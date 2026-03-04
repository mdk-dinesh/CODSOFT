from flask import Flask, render_template, request
import calculator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    num1 = None
    num2 = None
    operation = None

    if request.method == 'POST':
        try:
            num1_str = request.form.get('num1')
            num2_str = request.form.get('num2')
            operation = request.form.get('operation')

            if not num1_str or not num2_str:
                error = "Please enter both numbers."
            else:
                num1 = float(num1_str)
                num2 = float(num2_str)

                if operation == 'add':
                    result = calculator.add(num1, num2)
                    op_symbol = "+"
                elif operation == 'subtract':
                    result = calculator.subtract(num1, num2)
                    op_symbol = "-"
                elif operation == 'multiply':
                    result = calculator.multiply(num1, num2)
                    op_symbol = "*"
                elif operation == 'divide':
                    result = calculator.divide(num1, num2)
                    op_symbol = "/"
                else:
                    error = "Invalid operation selected."
                
                if result is not None:
                    # Format result to avoid unnecessary decimals like 5.0
                    if result.is_integer():
                        result = int(result)

        except ValueError as e:
            error = str(e)
        except Exception as e:
            error = f"An unexpected error occurred: {e}"

    return render_template('index.html', result=result, error=error, num1=num1, num2=num2, operation=operation)

if __name__ == '__main__':
    app.run(debug=True)
