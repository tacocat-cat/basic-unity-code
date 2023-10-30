using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public float speed = 10.0f;
    public float sensitivity = 5.0f;
    public float jumpHeight = 2.0f;

    private float moveFB;
    private float moveLR;

    private float rotX;
    private float rotY;

    private Vector3 movement;
    private Rigidbody rb;

    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    void Update()
    {
        moveFB = Input.GetAxis("Vertical") * speed;
        moveLR = Input.GetAxis("Horizontal") * speed;

        rotX = Input.GetAxis("Mouse X") * sensitivity;
        rotY -= Input.GetAxis("Mouse Y") * sensitivity;
        rotY = Mathf.Clamp(rotY, -60f, 60f);

        movement = new Vector3(moveLR, 0, moveFB);

        movement = transform.rotation * movement;

        rb.AddForce(movement);

        transform.eulerAngles = new Vector3(0, rotX, 0);

        Camera.main.transform.localRotation = Quaternion.Euler(rotY, 0, 0);

        if (Input.GetKeyDown(KeyCode.Space))
        {
            rb.AddForce(Vector3.up * jumpHeight, ForceMode.Impulse);
        }
    }
}
