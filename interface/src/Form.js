import React, { useState, useEffect } from 'react';
import bluePrint from './imagem_tcc.png';
import './Form.css';
import 'materialize-css/dist/css/materialize.min.css';
import io from "socket.io-client";


const endPoint = "http://localhost:5000";
const socket = io.connect(`${endPoint}`);

const Form = () => 
{
    const red = "rgb(158, 0, 0)";
    const green = "rgb(0, 177, 0)"
    const [machineId, setMachineId] = useState("");
    const [position, setPosition] = useState("No data");
    const [positionsColor, setPositionColor] = useState([red, red, red, red]);

    useEffect(() => {
        getPosition();
    }, [position]);

    const onChange = e => {
        setMachineId(e.target.value);
    };

    const getPosition = () => {
        socket.on("monitoring", res => {
                setPosition(res);
        });
        changeColor(position, green);
    };

    const changeColor = (pos, color) => {
        let newPositionsColor = positionsColor;
        newPositionsColor[pos] = color;
        setPositionColor([...newPositionsColor], newPositionsColor);
        if(color === red)
                return;
        setTimeout(() => {changeColor(pos, red)}, 1000);
    };

    const submit = () => {
        socket.emit("monitoring", machineId);
        setPosition("");
    };


    return(
            <div className="row" id="wrapper">
                <div className="row col s3">
                <div className="input-field col s6">
                        <input value={machineId} id="first_name2" type="text" className="validate" 
                            onChange = {e => onChange(e)}/>
                        <label className="active" htmlFor="first_name2">Id Maquina</label>
                            <button className="btn" onClick={() => submit()}>Enviar</button>
                    </div>
                </div>
                <div className="card-image card large col s9">
                    <span className="p1" style={{color: positionsColor[0]}}>&#9679;</span>
                    <span className="p2" style={{color: positionsColor[1]}}>&#9679;</span>
                    <span className="p3" style={{color: positionsColor[2]}}>&#9679;</span>
                    <span className="p4" style={{color: positionsColor[3]}}>&#9679;</span>
                    {/*<span className="p5" style={{color: this.state.cor}}>&#9679;</span>
                    <span className="p6" style={{color: this.state.cor}}>&#9679;</span>
                    <span className="p7" style={{color: this.state.cor}}>&#9679;</span>
                            <span className="p8" style={{color: this.state.cor}}>&#9679;</span>*/}
                    <img src={bluePrint} alt="Imagem não encontrada"/>
                    {/* <span class="card-title">Card Title</span> */}
                    {/*  rgb(0,100,0) cor verde */}
                </div>
            </div>
            
    );
};

export default Form;
