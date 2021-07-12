import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faExternalLinkAlt, faSignInAlt } from "@fortawesome/free-solid-svg-icons";
import { Col, Row, Image, Button, Container,  Navbar, Nav} from '@themesberg/react-bootstrap';
import { Link } from 'react-router-dom';
import { HashLink } from 'react-router-hash-link';

import { Routes } from "../routes";
import ReactHero from "../assets/img/technologies/react-hero-logo.svg";

export default () => {
  
  return (
    <>
      <Navbar variant="dark" expand="lg" bg="dark" className="navbar-transparent navbar-theme-primary sticky-top">
        <Container className="position-relative justify-content-between px-3">
          <Navbar.Brand as={HashLink} to="#home" className="me-lg-3 d-flex align-items-center">
            <Image src={ReactHero} />
            <span className="ms-2 brand-text d-none d-md-inline">PMS</span>
          </Navbar.Brand>

          <div className="d-flex align-items-center">
            <Navbar.Collapse id="navbar-default-primary">
              <Nav className="navbar-nav-hover align-items-lg-center">
                <Nav.Link as={HashLink} to="#features">About</Nav.Link>
                <Nav.Link as={HashLink} to="#pages">Contact Us</Nav.Link>
              </Nav>
            </Navbar.Collapse>
            <Button as={Link} to={Routes.Signin.path} variant="outline-white" className="ms-3"><FontAwesomeIcon icon={faSignInAlt} className="me-1" /> Login</Button>
          </div>
        </Container>
      </Navbar>
      <section className="section-header overflow-hidden pt-5 pt-lg-6 pb-9 pb-lg-12 bg-primary text-white" id="home">
        <Container>
          <Row>
            <Col xs={12} className="text-center">
              <div className="react-big-icon d-none d-lg-block"><span className="fab fa-react"></span></div>
              <h1 className="fw-bolder text-secondary">Parcel Management System</h1>
              <p className="text-muted fw-light mb-5 h5">A computerized and efficient parcel management service!</p>
              <br/>
              <p className="text-muted fw-light mb-5 h5">If its your first time please...</p>
              <div className="d-flex align-items-center justify-content-center">
                <Button variant="secondary" as={Link} to={Routes.Signup.path} className="text-dark me-3">
                  Sign Up <FontAwesomeIcon icon={faExternalLinkAlt} className="d-none d-sm-inline ms-1" />
                </Button>
              </div>
            </Col>
          </Row>
          <figure className="position-absolute bottom-0 left-0 w-100 d-none d-md-block mb-n2">
            <svg className="fill-soft" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3000 185.4">
              <path d="M3000,0v185.4H0V0c496.4,115.6,996.4,173.4,1500,173.4S2503.6,115.6,3000,0z" />
            </svg>
          </figure>
        </Container>
      </section>
      <footer className="footer py-6 bg-dark text-white">
        <Container>
          <Row>
            <Col className="mb-md-2">
              <div className="d-flex text-center justify-content-center align-items-center" role="contentinfo">
                <p className="font-weight-normal font-small mb-0">Copyright © PMS 2019-<span className="current-year">2021</span>. All rights reserved.</p>
              </div>
            </Col>
          </Row>
        </Container>
      </footer>
    </>
  );
};
