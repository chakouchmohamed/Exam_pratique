console.log("hello !!!")
d3.csv("data/data.csv")
    .row((d,i)=>{
        return{
                product_ID:d.product_ID,
                type:d.type,
                Air_temperature:d.Air_temperature,
                Process_temperature:d.Process_temperature,
                Rotational_speed:d.Rotational_speed,
                Torque:d.Torque,
                Tool_wear:d.Tool_wear
             };
})

.get((error,rows)=>{console.log("loaded"+rows.length+" rows")
if(rows.length>0){
    //console.log("First row: ",rows[0]);
   // console.log("Last row: ",rows[rows.length-1]);
    dataset=rows; 
    console.log(dataset);
}
});