class Resistor{
    protected width: number;
    protected height: number=40;
    protected u: number=0;
    protected i: number=0;
    protected p: number=0;
    constructor(protected r: number, protected g:any, 
         protected startx: number, protected endx: number, 
          protected y: number){
        this.width=this.endx-this.startx;
        this.draw();
    }
    draw(){
        this.g.clearRect(this.startx, this.y-this.height*2/3-10, this.width, this.height+20);
        this.g.beginPath();
        this.g.moveTo(this.startx, this.y);
        this.g.lineTo(this.startx+this.width/4, this.y);
        this.g.rect(this.startx+this.width/4, this.y-this.height/3, this.width/2, this.height*2/3);
        this.g.moveTo(this.startx+this.width*3/4, this.y);
        this.g.lineTo(this.endx, this.y);
        this.g.stroke();
        this.g.fillText(this.r+" Ω", this.startx+this.width/3, this.y+3);
        this.g.fillText(this.u+" V, "+this.i.toFixed(3)+" A", this.startx+this.width/4, this.y-this.height/3);
        this.g.fillText(this.p.toFixed(3)+" W", this.startx+this.width/4, this.y+this.height/3);
    }
    setR(r:number){
        this.r=r;
        this.calculate();
        this.draw();
    }
    getR():number{
        return this.r;
    }
    setU(u: number){
        this.u=u;
        this.calculate();
        this.draw()
    }
    getU():number{
        return this.u;
    }
    calculate(){
        this.calculateCurrent()
        this.calculatePower()
    }
    calculateCurrent(){
        this.i=this.u/this.r;
    }
    calculatePower(){
        this.p=this.u*this.i;
    }

}