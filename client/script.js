const isEmpty = (str) => !str.trim().length;
document.querySelector("button").disabled = true;

document
  .getElementById("form-food" && "form-food")
  .addEventListener("input", function () {
    if (isEmpty(this.value)) {
      console.log("NAME is invalid (Empty)");
      document.querySelector("button").disabled = true;
    } else {
      console.log(`NAME value is: ${this.value}`);
      document.querySelector("button").disabled = false;
    }
  });

  function ValidateActinsert() {
    var specialChars = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;
    if (document.actorInsert.actInsert.value.match(specialCahrs)) {
        alert ("Only characters A-Z, a-z and 0-9 are allowed!")
        document.actorInsert.actInsert.focus();
        return false;
    }
    return (true);
  }