from flask import Flask, render_template, request, jsonify
from cli_tasker.utils import *
app = Flask(__name__)

# API 示例: 新增任務
@app.route('/add-task', methods=['POST'])
def add():
    try:
        data = request.json
        name = data['name']
        print(name)
        
        if not name:
            return jsonify({"error": "Missing input"}), 400
        # 呼叫 CLI 功能
        add_task(name)

        # 回傳成功結果
        return jsonify({"message": "Task added successfully!", "task": name}), 201

    except Exception as e:
        print(f"Error: {str(e)}")  # 印出完整的錯誤訊息
        return jsonify({"error": str(e)}), 500
    

# 渲染首頁
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
