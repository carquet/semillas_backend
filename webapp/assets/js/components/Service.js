import React, { PropTypes } from 'react'
import { Link } from 'react-router'

const Service = ({ service }) => {
  const { title, description, uuid } = service

  return (
    <div className="Service">
        <Link to={`ismaell/ismael`}>
          {uuid}
        </Link>

     {description &&
        <p>{description}</p>

      }
    </div>
  )
}

Service.propTypes = {
  //uuid: PropTypes.string.isRequired,
  //description: PropTypes.string

  service: PropTypes.shape({
    uuid: PropTypes.string.isRequired,
    description: PropTypes.string
  }).isRequired,
}

export default Service
