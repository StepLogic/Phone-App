import axios from "axios";
const instance = axios.create({
  baseURL: "http://localhost:8000",
});
export const getAllContacts = async () => {
  return instance.get("/contacts/list/all").then((res) => res.data);
};

export const createContact = async ({ firstName, lastName, phone }) => {
  console.log(
    "Local",
    process.env.REACT_BASE_API_URL || "http://localhost:8000"
  );
  return instance
    .post("/contacts/create", {
      first_name: firstName,
      last_name: lastName,
      phone: phone,
    })
    .then((res) => res.data);
};
