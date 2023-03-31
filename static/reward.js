function redeemPoints() {
  var points = parseInt(document.getElementById("points").value);
  var result = document.getElementById("result");

  if (isNaN(points) || points < 0) {
    result.innerHTML = "Please enter a valid number of points.";
  } else {
    var giftCards = Math.floor(points / 10);
    var remainingPoints = points % 10;
    result.innerHTML = "Congratulations! You have earned " + giftCards + " gift card(s) and have " + remainingPoints + " point(s) remaining.";
  }
}
