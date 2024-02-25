import express from 'express';
import { AppController } from '../controllers/AppController.js';
import { StudentsController } from '../controllers/StudentsController.js';

const router = express.Router();

// Link the route '/' to the AppController
router.get('/', AppController.getHomepage);

// Link the route '/students' to the StudentsController
router.get('/students', StudentsController.getAllStudents);

// Link the route '/students/:major' to the StudentsController
router.get('/students/:major', StudentsController.getAllStudentsByMajor);

export default router;
