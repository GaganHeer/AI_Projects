using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

/*
    Gagan Heer A00933997
    Decision Making: State Machine
    Please look over the README.md file there is any trouble using this file
*/

public class StateMachine : MonoBehaviour
{

    public GameObject p1;
    public GameObject p2;
    public GameObject bullet;
    public Text result;
    public Button playAgain;
    private State currentState = State.PATROL;
    public float playerSpd;
    public float enemySpd;
    private float clockwise = 250.0f;
    private float counterClockwise = -250.0f;
    private float rotSpd = 100.0f;    
    private bool movingUp = true;
    private bool shooting = true;
    private bool gameOver = false;
    private int reloadDelay = 0;    
    private int shootDelay = 0;
    private int ammo = 3;

    enum State
    {
        PATROL,
        CHASE,
        FIRE
    }

    void Start()
    {
        playerSpd = 25.0f;
        enemySpd = 15.0f;
        result.gameObject.SetActive(false);
        playAgain.onClick.AddListener(restartLevel);
        playAgain.gameObject.SetActive(false);
    }

    void Update()
    {
        if (!gameOver)
        {
            P1Controls();
            float distBetween = Vector3.Distance(p1.transform.position, p2.transform.position);
            print(distBetween);

            //Enemy will change state to FIRE
            if (distBetween <= 40)
            {
                //If changing from chasing to firing then reduce spd in order to aim
                if (currentState == State.CHASE)
                {
                    enemySpd = 5.0f;
                }
                currentState = State.FIRE;
            }
            //Enemy will change state to CHASE
            else if (distBetween > 40 && distBetween <= 100)
            {
                //If changing from firing to chasing then reduce spd so player has a chance to get away
                if (currentState == State.FIRE)
                {
                    enemySpd = 5.0f;
                }

                //If changing from patrolling to chasing then increase spd in order to catch up to player
                if (currentState == State.PATROL)
                {
                    enemySpd = 15.0f;
                }
                currentState = State.CHASE;
            }
            //Enemy will change state to PATROL
            else
            {
                //If changing from chasing to patrolling then reset spd
                if (currentState == State.CHASE)
                {
                    enemySpd = 15.0f;
                }
                currentState = State.PATROL;
            }

            if (currentState == State.PATROL)
            {
                print("PATROL");
                p2.transform.rotation = Quaternion.Slerp(p2.transform.rotation, Quaternion.identity, Time.deltaTime * rotSpd);

                if (p2.transform.position.z >= 80)
                {
                    movingUp = false;
                }

                if (p2.transform.position.z <= -80)
                {
                    movingUp = true;
                }

                if (movingUp)
                {
                    p2.transform.Translate(new Vector3(0, 0, enemySpd * 2) * Time.deltaTime);
                }
                else
                {
                    p2.transform.Translate(new Vector3(0, 0, -enemySpd * 2) * Time.deltaTime);
                }

            }
            else if (currentState == State.CHASE)
            {
                print("CHASE");
                P2Chasing(enemySpd * 3);
            }
            else if (currentState == State.FIRE)
            {
                print("FIRE");
                P2Chasing(enemySpd);

                if (shooting)
                {
                    if (shootDelay < 30)
                    {
                        shootDelay++;
                    }
                    else
                    {
                        shootDelay = 0;
                        shooting = false;
                    }

                }

                if (reloadDelay < 150)
                {
                    if (ammo > 0 && !shooting)
                    {
                        shooting = true;
                        GameObject newBullet = Instantiate(bullet, p2.transform.position + (p2.transform.forward * 10), p2.transform.rotation);
                        newBullet.GetComponent<Rigidbody>().AddForce((p1.transform.position - newBullet.transform.position) * 150);
                        ammo--;
                    }
                }
                else if (reloadDelay >= 100)
                {
                    reloadDelay = 0;
                    ammo = 3;
                }
                reloadDelay++;
            }
        }

    }

    void OnCollisionEnter(Collision col)
    {
        if (col.gameObject.name == "goal")
        {
            gameEndEvents("YOU WIN");
        }
        else if (col.gameObject.name.Contains("bullet"))
        {
            gameEndEvents("YOU LOSE");
        }
    }

    void P1Controls()
    {
        if (Input.GetKey(KeyCode.W))
        {
            p1.transform.position += transform.forward * Time.deltaTime * playerSpd;
        }
        else if (Input.GetKey(KeyCode.S))
        {
            p1.transform.position -= transform.forward * Time.deltaTime * playerSpd;
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

    void P2Chasing(float spd)
    {
        Vector3 dir = (p1.transform.position - p2.transform.position).normalized;
        Quaternion rot = Quaternion.LookRotation(dir);
        p2.transform.rotation = Quaternion.Slerp(p2.transform.rotation, rot, Time.deltaTime * rotSpd);
        p2.transform.position = Vector3.MoveTowards(p2.transform.position, p1.transform.position, Time.deltaTime * spd);
    }

    void restartLevel()
    {
        SceneManager.LoadScene("SampleScene");
    }

    void gameEndEvents(string resultText)
    {
        result.text = resultText;
        result.gameObject.SetActive(true);
        gameOver = true;
        playAgain.gameObject.SetActive(true);
    }
}
