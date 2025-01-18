async function addTask() {
    const taskName = document.getElementById('task-name').value;
    if (!taskName) {
        alert('Please enter a task name.');
        return;
    }
    const response = await fetch('/add-task', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: taskName }),
    });
    const data = await response.json();
    if (data.message) {
        alert(data.message);
        // 更新任務列表 (需要呼叫一個 API 來獲取最新任務列表)
    }
}
