import React, { useState, useEffect } from "react";
import useAxios from "../../utils/axios";
import Table from "./listTable";
import { useNavigate } from "react-router-dom";
import { getTalks } from "../../services/talks";
import { trackPromise } from "react-promise-tracker";

const Talks = () => {
  let navigate = useNavigate();
  let api = useAxios();

  let [talks, setTalks] = useState([]);

  useEffect(() => {
    let mounted = true;
    trackPromise(
      getTalks(api)
        .then((response) => {
          if (mounted) {
            setTalks(response.data);
          }
        })
        .catch((error) => {
          if (mounted) {
            if (error.response.status === 401) {
              alert("Authentication has expired! Please re-login");
              navigate("/logout");
            } else {
              alert("Something went wrong! Please logout and try again");
            }
          }
        })
    );
    return () => {
      mounted = false;
    };
  }, []);

  if (!talks || talks.length === 0)
    return (
      <div className="text-center pt-5">
        <p className="text-xl text-bold">Can not find any talks, sorry</p>
      </div>
    );

  return <Table talks={talks} />;
};

export default Talks;
