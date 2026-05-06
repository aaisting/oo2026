class Resistor{
    protected r: number;
    protected g;
    constructor(r: number, g:any){
        this.r=r; 
        this.g=g;
        this.draw();
    }
    draw(){
        this.g.beginPath();
        this.g.rect(20, 10, 200, 60);
        this.g.stroke();
        this.g.fillText(""+this.r, 30, 20);
    }
}