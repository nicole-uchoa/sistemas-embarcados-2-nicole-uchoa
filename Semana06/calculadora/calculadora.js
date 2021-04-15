var valor;
var result;

function botao(num){
    valor = document.calc.visor.value += num;
}

function reset(){
    document.calc.visor;
}

function calcula(){
    result = eval(valor);
    document.calc.visor.value = result.toLocaleString('pt-br');
}