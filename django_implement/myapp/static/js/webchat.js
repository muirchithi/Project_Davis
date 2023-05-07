// get the form and input field
const form = document.querySelector('#chat-form');
const input = document.querySelector('#chat-input');

// get the chat log element
const chatLog = document.querySelector('#chat-log');

// create a WebSocket connection
const socket = new WebSocket('ws://localhost:8000/ws/chat/');

// send a message when the form is submitted
form.addEventListener('submit', (event) => {
    event.preventDefault();
    const message = input.value.trim();
    if (message) {
        socket.send(JSON.stringify({
            'type': 'chat.message',
            'content': message
        }));
        input.value = '';
    }
});

// handle incoming messages
socket.addEventListener('message', (event) => {
    const message = JSON.parse(event.data);
    if (message.type === 'chat.message') {
        const sender = message.sender;
        const content = message.content;
        const timestamp = new Date(message.timestamp).toLocaleString();
        const html = `<p><strong>${sender}</strong> <em>${timestamp}</em><br>${content}</p>`;
        chatLog.insertAdjacentHTML('beforeend', html);
        chatLog.scrollTop = chatLog.scrollHeight;
    }
});
