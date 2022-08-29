const box = document.getElementById("box")
const img = document.getElementById("imgMapaPrincipal")

box.addEventListener("mousemove", (e) =>{
    const x = e.clientX - e.target.offsetLeft;
    const y = e.clientY - e.target.offsetTop;

    // retorna um erro se ocorrer //
    console.log(x, y);
    console.log('olá');

    img.style.transformOrigin = `${x}px ${y}px`;
    img.style.transform = "scale(2)";
});

box.addEventListener("mouseleave", () =>{

    img.style.transformOrigin = "center center";
    img.style.transform = "scale(1)";
})