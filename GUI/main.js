document.getElementsByClassName('back_arrow')[0].addEventListener('click',() => {
    location.reload();
});

function chooseBrowser(){
    let browser = document.getElementsByClassName("choose-button");
    for(let i=0; i<browser.length; i++){
        browser[i].onclick = () =>{
        var org = browser[i].value;
        if(org == 'Chrome'){
            chromeStart('/chrome.js')
        }
        else{
            ffStart('/firefox.js')
        }
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
        };
    }
    }

function chromeStart(src){
    let script = document.createElement('script');
    script.src = src;
    script.async = false;
    document.head.appendChild(script);
}

function ffStart(src){
    let script = document.createElement('script');
    script.src = src;
    script.async = false;
    document.head.appendChild(script);
}


chooseBrowser();
