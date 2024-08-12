let currentDiv = 1;

function outputDiv()
{
  document.querySelector(".outputTextSection").style.display = "none";
  document.querySelector(".outputReplayButton").style.display = "none";
}

function outputContributionDiv()
{
  document.querySelector(".outputTextSection").style.display = "none";
}

function nextDiv()
{
  if (!validateCurrentDiv(currentDiv)) return;

  disableAllDivs();
  currentDiv++;
  updateProgress();
  document.getElementById(`div${currentDiv}`).classList.remove("disableDiv");

  if (currentDiv > 1)
  {
    document.getElementById("btnPrev").classList.remove("disableDiv");
  }
  if (currentDiv === 8)
  {
    document.getElementById("btnNext").classList.add("disableDiv");
  }
}

function previousDiv()
{
  disableAllDivs();
  currentDiv--;
  updateProgress();
  document.getElementById(`div${currentDiv}`).classList.remove("disableDiv");

  if (currentDiv === 1)
  {
    document.getElementById("btnPrev").classList.add("disableDiv");
  }
  if (currentDiv < 8)
  {
    document.getElementById("btnNext").classList.remove("disableDiv");
  }
}

function disableAllDivs()
{
  for (let i = 1; i <= 8; i++)
  {
    document.getElementById(`div${i}`).classList.add("disableDiv");
  }
}

function validateCurrentDiv(divNumber)
{
  const inputs = document.querySelectorAll(`#div${divNumber} input`);
  for (const input of inputs)
  {
    if (!input.checkValidity())
    {
      input.reportValidity();
      return false;
    }
  }
  return true;
}

function updateProgress()
{
  const progressValue = (currentDiv / 8) * 100;
  document.getElementById("progress").value = progressValue;
  document.getElementById("progress").innerText = `${progressValue}%`;
}

export { nextDiv, previousDiv, outputDiv, outputContributionDiv }
