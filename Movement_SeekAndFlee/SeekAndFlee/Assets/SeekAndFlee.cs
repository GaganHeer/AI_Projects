using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/*
    Gagan Heer A00933997
    Movement: Seek and Flee
    Please look over the README.md file if there is any trouble using this file
*/

public class SeekAndFlee : MonoBehaviour
{

    public GameObject p1;
    public GameObject p2;
    public float clockwise = 250.0f;
    public float counterClockwise = -250.0f;
    public float rotSpd = 100.0f;
    public float seekSpd;
    public float fleeSpd;
    public bool p1Seeking = false;
    public bool p1Paused = false;
    public bool p2Paused = true;
    public float pauseTimer = 0;

    void Start()
    {
        seekSpd = 25.0f;
        fleeSpd = 15.0f;
    }

    void Update()
    {

        if (p1Seeking)
        {
            if(p2Paused == false)
            {
                p2.transform.LookAt(p1.transform);
                p2.transform.Rotate(0, 180, 0);
                p2.transform.Translate(new Vector3(0, 0, fleeSpd) * Time.deltaTime);
            }

            if (p1Paused == false)
            {
                // Uncomment for P1 automatic movement
                /*Vector3 dir2 = (p2.transform.position - p1.transform.position).normalized;
                Quaternion rot2 = Quaternion.LookRotation(dir2);
                p1.transform.rotation = Quaternion.Slerp(p1.transform.rotation, rot2, Time.deltaTime * rotSpd);
                p1.transform.position = Vector3.MoveTowards(p1.transform.position, p2.transform.position, Time.deltaTime * seekSpd);*/

                P1Controls();
            }
            else
            {
                pauseTimer += 1;
                if (pauseTimer >= 100)
                {
                    pauseTimer = 0;
                    p1Paused = false;
                }
            }
        }
        else
        {
            if(p1Paused == false)
            {
                // Uncomment for P1 automatic movement
                /*p1.transform.LookAt(p2.transform);
                p1.transform.Rotate(0, 180, 0);
                p1.transform.Translate(new Vector3(0, 0, fleeSpd) * Time.deltaTime);*/

                P1Controls();
            }

            if (p2Paused == false)
            {
                Vector3 dir2 = (p1.transform.position - p2.transform.position).normalized;
                Quaternion rot2 = Quaternion.LookRotation(dir2);
                p2.transform.rotation = Quaternion.Slerp(p2.transform.rotation, rot2, Time.deltaTime * rotSpd);
                p2.transform.position = Vector3.MoveTowards(p2.transform.position, p1.transform.position, Time.deltaTime * seekSpd);
            }
            else
            {
                pauseTimer += 1;
                if(pauseTimer >= 100)
                {
                    pauseTimer = 0;
                    p2Paused = false;
                }
            }
        }
    }

    void OnCollisionEnter(Collision col)
    {
        if (col.gameObject.name == "p2")
        {
            if (p1Seeking)
            {
                p2Paused = true;
                p1Paused = false;
            }
            else
            {
                p1Paused = true;
                p2Paused = false;
            }
            p1Seeking = !p1Seeking;
        }
    }

    void P1Controls()
    {
        if (Input.GetKey(KeyCode.W))
        {
            p1.transform.position += transform.forward * Time.deltaTime * seekSpd;
        }
        else if (Input.GetKey(KeyCode.S))
        {
            p1.transform.position -= transform.forward * Time.deltaTime * seekSpd;
        }

        if (Input.GetKey(KeyCode.A))
        {
            p1.transform.Rotate(0, Time.deltaTime * clockwise, 0);
        }
        else if (Input.GetKey(KeyCode.D))
        {
            p1.transform.Rotate(0, Time.deltaTime * counterClockwise, 0);
        }
    }
}
