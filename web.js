async function send_msg(){
    let chat_id = document.getElementById('chat_id').value;
    let msg = document.getElementById('message').value;

    let result = await eel.send_message(chat_id,massage)();

    document.getElementById('result').innerHTML = result;

    $('#send_message').on('click',function(){
        send_msg();
    });
}