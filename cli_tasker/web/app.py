from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# API 示例: 新增任務
@app.route('/add-task', methods=['POST'])
def add_task():
    data = request.json
    # 在此處調用你的 CLI 方法
    return jsonify({"message": "Task added successfully!", "task": data})

# 渲染首頁
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
