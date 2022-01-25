function sendDevData() {
    let btns = document.getElementsByClassName('dev');
    for(let i=0; i<btns.length; i++){
        btns[i].onclick = () =>{
        let org = btns[i].value;
        eel.login_dev_ff(org);
        };
    }
}

function sendQAData() {
    let btns = document.getElementsByClassName('qa');
    for(let i=0; i<btns.length; i++){
        btns[i].onclick = () =>{
        let org = btns[i].value;
        eel.login_qa_ff(org);
        };
    }
}

function sendProdData() {
    let btns = document.getElementsByClassName('prod');
    for(let i=0; i<btns.length; i++){
        btns[i].onclick = () =>{
        let org = btns[i].value;
        eel.login_prod_ff(org);
        };
    }
}



sendDevData();
sendQAData();
sendProdData();