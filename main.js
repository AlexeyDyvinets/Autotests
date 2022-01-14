
document.getElementById('chrome').addEventListener('click', () =>{
    eel.logChrome()
    var firstScreen = document.getElementById('buttons');
    firstScreen.remove();
    document.getElementById('orgs').style.display = "flex";
    document.getElementsByClassName('back_arrow')[0].style.display = "flex";
    new Skroll()
    .add(".org-column",{
        delay:10,
        duration:600,
        animation:"ZoomIn"
    })
    .init();
});


document.getElementById('firefox').addEventListener('click', () =>{
    eel.logFF()
    var firstScreen = document.getElementById('buttons');
    firstScreen.remove();
    document.getElementById('orgs').style.display = "flex";
    document.getElementsByClassName('back_arrow')[0].style.display = "flex";
    new Skroll()
    .add(".org-column",{
        delay:10,
        duration:600,
        animation:"ZoomIn"
    })
    .init();
});

document.getElementsByClassName('back_arrow')[0].addEventListener('click',() => {
    location.reload();
});
// function chooseBrowser(){

//     // for(let i=0; i<browser.length; i++){
//     //     browser[i].onclick = () => {
//     //         if (browser[i].value == "Chrome"){
//     //             dir = "chrome";
//     //         }
//     //         else if(browser[i].value == "Firefox"){
//     //             dir = "firefox";
//     //         }
//     //         eel.login(dir)
 

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

// chooseBrowser();
