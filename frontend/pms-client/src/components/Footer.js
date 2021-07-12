
import React from "react";
import moment from "moment-timezone";
import { Row, Col, Card } from '@themesberg/react-bootstrap';

import { HashLink } from 'react-router-hash-link';

export default (props) => {
  const currentYear = moment().get("year");

  return (
    <div>
      <footer className="footer section py-5">
        <Row>
          <Col xs={12} lg={6} className="mb-4 mb-lg-0">
            <p className="mb-0 text-center text-xl-left">
              Copyright © 2019-{`${currentYear} `}
              <Card.Link as={HashLink} to="#home" target="_blank" className="text-blue text-decoration-none fw-normal">
                PMS
            </Card.Link>
            </p>
          </Col>
          <Col xs={12} lg={6}>
            <ul className="list-inline list-group-flush list-group-borderless text-center text-xl-right mb-0">
              <li className="list-inline-item px-0 px-sm-2">
                <Card.Link  as={HashLink} to="#about">
                  About
              </Card.Link>
              </li>
              <li className="list-inline-item px-0 px-sm-2">
                <Card.Link as={HashLink} to="#home">
                  Contact
              </Card.Link>
              </li>
            </ul>
          </Col>
        </Row>
      </footer>
    </div>
  );
};
