import React, {useState} from 'react'
import Stack from 'react-bootstrap/Stack'
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import "./formCar.css"
import api from '../../services/api'
import Card from 'react-bootstrap/Card'
import Spinner from 'react-bootstrap/Spinner'

export default function FormCar() {


    const [state, setstate] = useState(null)
    const [plate, setplate] = useState(null)
    const [loader, setLoader] = useState(false)

    const handleChanges = (event) => {
        setstate(event.target.value);
    };

    const handleSubmit = async() =>{
        setLoader(true)
        const response = await api.car.getOne(state).then(response => {
            return { car: response.data.objects[0]}
        }).catch(err => {
           console.log('Ups, tuvimos un problema.')
        });
        setplate(response.car?response.car.name:'No existe esta patente en nuestra base')
        setLoader(false)
    }
    return (
        <>
            <Row className="row-car">
                <h2>Buscar Modelo</h2>
            </Row>
            <Row>
                <Col className="col-car">
                    <Stack direction="horizontal" gap={3}>
                        <Form.Control className="me-auto" onChange={handleChanges} placeholder="cargue su patente...ej: AAA123" />
                            <Button onClick={handleSubmit}  variant="secondary">Submit</Button>
                            <div className="vr" />
                    </Stack>
                </Col>
            </Row>
            <Row className="row-card">
                <Card>
                    <Card.Body>
                        <Card.Title>Modelo</Card.Title>
                        {loader?
                            <Spinner animation="border" role="status">
                                <span className="visually-hidden">Loading...</span>
                            </Spinner>:
                            <Card.Text>
                                {plate}
                            </Card.Text>
                        }
                        </Card.Body>
                </Card>
            </Row>
        </>
    )
}