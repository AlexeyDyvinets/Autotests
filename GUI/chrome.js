function sendDevData() {
    let btns = document.getElementsByClassName('dev');
    for(let i=0; i<btns.length; i++){
        btns[i].onclick = () =>{
        let org = btns[i].value;
        eel.login_dev_ch(org);
        };
    }
}

function sendQAData() {
    let btns = document.getElementsByClassName('qa');
    for(let i=0; i<btns.length; i++){
        btns[i].onclick = () =>{
        let org = btns[i].value;
        eel.login_qa_ch(org);
        };
    }
}

function sendProdData() {
    let btns = document.getElementsByClassName('prod');
    for(let i=0; i<btns.length; i++){
        btns[i].onclick = () =>{
        let org = btns[i].value;
        eel.login_prod_ch(org);
        };
    }
}



sendDevData();
sendQAData();
sendProdData();