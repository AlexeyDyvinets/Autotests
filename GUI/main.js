function sendDevData() {
    let btns = document.getElementsByClassName('dev');
    for(let i=0; i<btns.length; i++){
        btns[i].onclick = () =>{
        let org = btns[i].value;
        eel.login_dev(org);
        };
    }
}

function sendQAData() {
    let btns = document.getElementsByClassName('qa');
    for(let i=0; i<btns.length; i++){
        btns[i].onclick = () =>{
        let org = btns[i].value;
        eel.login_qa(org);
        };
    }
}

function sendProdData() {
    let btns = document.getElementsByClassName('prod');
    for(let i=0; i<btns.length; i++){
        btns[i].onclick = () =>{
        let org = btns[i].value;
        eel.login_prod(org);
        };
    }
}

sendDevData();
sendQAData();
sendProdData();

