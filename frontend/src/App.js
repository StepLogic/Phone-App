import "./App.css";

import {
  Typography,
  Container,
  Box,
  Table,
  TableHead,
  TextField,
  TableRow,
  TableCell,
  Stack,
  Button,
  Divider,
  TableBody,
} from "@mui/material";
import React, { useState } from "react";

import { useFormik } from "formik";
import * as yup from "yup";
import { createContact } from "./api/Contacts";

const validationSchema = yup.object({
  firstName: yup.string("Enter First Name").required("First Name is required"),
  lastName: yup.string("Enter Last Name").required("Last Name is required"),
  phone: yup.string("Enter Phone Number").required("Phone Number is required"),
});

function App() {
  // const redTheme = createTheme({ palette: { primary: red } });
  const formik = useFormik({
    initialValues: {
      firstName: "Omic",
      lastName: "Rocks",
      phone: "5558675309",
    },
    validationSchema: validationSchema,
    onSubmit: (values) => {
      createContact(values)
        .then((data) => {
          // setExistingContacts((state) => {
          //   console.log("Data", data);
          //   state.push(data);
          //   console.log("Data", state);
          //   return state;
          // });
          setExistingContacts([...existingContacts, data]);
          // console.log("Data", data);
        })
        .catch((err) => {
          console.log("Error Creating Contact", err);
        });
    },
  });
  const [existingContacts, setExistingContacts] = useState([]);
  // useEffect(() => {}, []);
  return (
    // <ThemeProvider theme={redTheme}>
    <Box
      display="flex"
      justifyContent="center"
      alignItems="center"
      minHeight="100vh"
    >
      <Container maxWidth="lg" sx={{ margin: "auto" }}>
        <Stack
          spacing={2}
          direction={{ xs: "column", sm: "row" }}
          divider={<Divider orientation="vertical" flexItem />}
        >
          <Stack spacing={3} width={{ lg: "50%", xs: "100%" }}>
            <Typography
              variant="h5"
              component="h1"
              gutterBottom
              align="center"
              color="primary"
            >
              Phone Book App
            </Typography>
            <form onSubmit={formik.handleSubmit}>
              <Stack spacing={2}>
                <TextField
                  id="outlined-basic"
                  label="First Name"
                  name="firstName"
                  variant="standard"
                  // color="secondary"
                  value={formik.values.firstName}
                  onChange={formik.handleChange}
                  error={
                    formik.touched.firstName && Boolean(formik.errors.firstName)
                  }
                  helperText={
                    formik.touched.firstName && formik.errors.firstName
                  }
                />
                <TextField
                  id="outlined-basic"
                  label="Last Name"
                  name="lastName"
                  variant="standard"
                  // color="secondary"
                  value={formik.values.lastName}
                  onChange={formik.handleChange}
                  error={
                    formik.touched.lastName && Boolean(formik.errors.lastName)
                  }
                  helperText={formik.touched.lastName && formik.errors.lastName}
                />
                <TextField
                  name="phone"
                  id="outlined-basic"
                  label="Phone"
                  type={"tel"}
                  variant="standard"
                  value={formik.values.phone}
                  onChange={formik.handleChange}
                  error={formik.touched.phone && Boolean(formik.errors.phone)}
                  helperText={formik.touched.phone && formik.errors.phone}
                />
                <Button
                  color="primary"
                  size="medium"
                  variant="outlined"
                  type="submit"
                >
                  Add User
                </Button>
              </Stack>
            </form>
          </Stack>
          <Box sx={{ my: 4 }} width={{ lg: "50%", xs: "100%" }}>
            <Table>
              <TableHead>
                <TableRow>
                  <TableCell>First Name</TableCell>
                  <TableCell>Last Name</TableCell>
                  <TableCell>Phone</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {existingContacts.map((contact) => (
                  <TableRow key={contact.id}>
                    <TableCell>{contact.first_name}</TableCell>
                    <TableCell>{contact.last_name}</TableCell>
                    <TableCell>{contact.phone}</TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </Box>
        </Stack>
      </Container>
    </Box>
    // </ThemeProvider>
  );
}

export default App;
