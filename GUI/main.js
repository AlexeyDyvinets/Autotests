let dev_int_btn = document.getElementById("dev_internal_but").onclick
= function dev_int_login(btn) {
    let x = btn.value;
    console.log(x)
    eel.dev_int_log()
}

let dev_ass_btn = document.getElementById("dev_asset_but").onclick
= function dev_ass_login() {
    eel.dev_ass_log()
}

let dev_cash_btn = document.getElementById("dev_cash_but").onclick
= function dev_cash_login() {
    eel.dev_cash_log()
}

let dev_fiig_btn = document.getElementById("dev_fiig_but").onclick
= function dev_fiig_login() {
    eel.dev_fiig_log()
}

// QA

let qa_int_btn = document.getElementById("qa_internal_but").onclick
= function qa_int_login() {
    eel.qa_int_log()
}

let qa_ass_btn = document.getElementById("qa_asset_but").onclick
= function qa_ass_login() {
    eel.qa_asset_log()
}

let qa_cash_btn = document.getElementById("qa_cash_but").onclick
= function qa_cash_login() {
    eel.qa_cash_log()
}


// PROD

let prod_fiig_btn = document.getElementById("asset_but").onclick
= function prod_ass_login() {
    eel.prod_ass_log()
}

