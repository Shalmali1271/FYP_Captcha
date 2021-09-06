document.addEventListener("DOMContentLoaded", function() {
  createRobotAnimation();
});

/* Robot Animations */
const createRobotAnimation = () => {
  console.log("robot animation function");
  lottie.loadAnimation({
    container: document.getElementById("robot"),
    path: "https://assets6.lottiefiles.com/packages/lf20_KdqVU9.json",
    renderer: "svg",
    loop: true,
    autoplay: true,
    name: "Hello Humans!"
  });
};