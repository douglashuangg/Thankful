// no clue whats happening here tbh

// document.addEventListener("DOMContentLoaded", () => {
//     document.querySelector("#form").onsubmit = (event) => {
//         event.preventDefault();
//         const request = new XMLHttpRequest();
//         request.onload = () => {
//             const data = JSON.parse(request.responseText);
//             if (data.success) {
//                 window.location.href = "/dashboard/";
//             }
//         }
//         const data = new FormData();
//         data.append('entry', document.querySelector('#entry').value);
//         request.open('POST', '/submitdata', true);
//         request.send(data);
//     }
// })