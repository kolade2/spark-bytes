const btn = (document.querySelector("button").disabled = true);
const isEmpty = (str) => !str.trim().length;

document
  .getElementById("form-location" && "form-food")
  .addEventListener("input", function () {
    if (isEmpty(this.value)) {
      console.log("NAME is invalid (Empty)");
      document.querySelector("button").disabled = true;
    } else {
      console.log(`NAME value is: ${this.value}`);
      document.querySelector("button").disabled = false;
    }
  });
