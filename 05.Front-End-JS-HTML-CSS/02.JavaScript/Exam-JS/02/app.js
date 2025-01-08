window.addEventListener("load", solve);

function solve() {
  const nextButton = document.getElementById("next-btn");
  const previewList = document.getElementById("preview-list");
  const eventList = document.getElementById("event-list");
  
  const [emailInput, eventInput, locationInput] = Array.from(document.querySelectorAll("input"));

  // Add an event listener for the [Next] button
  nextButton.addEventListener("click", () => {
      const email = emailInput.value.trim();
      const event = eventInput.value.trim();
      const location = locationInput.value.trim();

      // Validate input fields
      if (!email || !event || !location) return;

      // Disable [Next] button
      nextButton.disabled = true;

      // Clear input fields
      emailInput.value = "";
      eventInput.value = "";
      locationInput.value = "";

      // Create a new <li> structure
      const li = document.createElement("li");
      li.className = "application";

      const article = document.createElement("article");
      article.innerHTML = `
          <h4>${email}</h4>
          <p><strong>Event:</strong><br>${event}</p>
          <p><strong>Location:</strong><br>${location}</p>
      `;

      const editButton = document.createElement("button");
      editButton.className = "action-btn edit";
      editButton.textContent = "Edit";

      const applyButton = document.createElement("button");
      applyButton.className = "action-btn apply";
      applyButton.textContent = "Apply";

      li.appendChild(article);
      li.appendChild(editButton);
      li.appendChild(applyButton);

      previewList.appendChild(li);

      // Add event listeners for the [Edit] and [Apply] buttons
      editButton.addEventListener("click", () => {
          // Restore data to input fields
          emailInput.value = email;
          eventInput.value = event;
          locationInput.value = location;

          // Remove the <li> from preview list
          li.remove();

          // Enable [Next] button
          nextButton.disabled = false;
      });

      applyButton.addEventListener("click", () => {
          // Remove [Edit] and [Apply] buttons
          editButton.remove();
          applyButton.remove();

          // Move the <li> to the event list
          eventList.appendChild(li);

          // Enable [Next] button
          nextButton.disabled = false;
      });
  });
}
