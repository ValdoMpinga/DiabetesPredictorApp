//Handles form premature submit
function handlePrematureSubmit()
{
    const progress = document.getElementById("progress").value;
    if (progress !== 100)
    {
        alert('O formulário deve ser completamente preenchido antes de submetido');
        return false;
    }
    return true;
}

export { handlePrematureSubmit }
