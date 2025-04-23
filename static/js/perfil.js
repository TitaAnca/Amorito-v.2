document.addEventListener("DOMContentLoaded", () => {
    const editBtn = document.getElementById("edit-btn");
    const deleteBtn = document.getElementById("delete-btn");
    const editModal = document.getElementById("edit-modal");
    const closeEditModal = document.getElementById("close-edit-modal");
    const saveBtn = document.getElementById("save-btn");

    const username = document.getElementById("username");
    const handle = document.getElementById("handle");
    const location = document.getElementById("location");
    const memberDate = document.getElementById("member-date");
    const interests = document.getElementById("interests");

    const editUsername = document.getElementById("edit-username");
    const editHandle = document.getElementById("edit-handle");
    const editLocation = document.getElementById("edit-location");
    const editMemberDate = document.getElementById("edit-member-date");
    const editInterests = document.getElementById("edit-interests");

    editBtn.addEventListener("click", () => {
        editModal.style.display = "flex";
    });

    closeEditModal.addEventListener("click", () => {
        editModal.style.display = "none";
    });

    saveBtn.addEventListener("click", () => {
        username.innerText = editUsername.value;
        handle.innerText = editHandle.value;
        location.innerText = editLocation.value;
        memberDate.innerText = editMemberDate.value;
        interests.innerText = editInterests.value;

        editModal.style.display = "none";
    });
});


