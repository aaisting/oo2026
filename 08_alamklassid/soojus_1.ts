class MaterialAmount{
    mass: number;
    specificHeatCapacity:number;
    temperature: number;
    constructor(mass:number, specificHeatCapacity:number, temperature:number){
        this.mass=mass;
        this.specificHeatCapacity=specificHeatCapacity;
        this.temperature=temperature;
    }
    getTemperature(){
        return this.temperature;
    }
    changeEnergy(joules:number){
        this.temperature+=joules/(this.mass*this.specificHeatCapacity);
    }
}

let waterPot:MaterialAmount=new MaterialAmount(3, 4200, 20);
waterPot.changeEnergy(10000);
console.log(waterPot.getTemperature());
let ironRadiator:MaterialAmount=new MaterialAmount(10, 412, 20);
ironRadiator.changeEnergy(10000);
console.log(ironRadiator.getTemperature());
if(ironRadiator.getTemperature()>waterPot.getTemperature()){
   let changeAmount:number=1000;
   ironRadiator.changeEnergy(-changeAmount);
   waterPot.changeEnergy(changeAmount);
} 
console.log(waterPot.getTemperature(), ironRadiator.getTemperature());