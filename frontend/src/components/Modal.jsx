import "./CSS/Modals/Modal.css";

const Modal = ({ ShouldOpen, Onclose, children }) => {
  return (
    <>
      {ShouldOpen ? (
        <div
          className="Modal"
          onClick={() => {
            Onclose(false);
          }}
        >
          <div
            onClick={(event) => {
              event.stopPropagation();
            }}
          >
            {children}
          </div>
        </div>
      ) : (
        <div></div>
      )}
    </>
  );
};

export default Modal;
